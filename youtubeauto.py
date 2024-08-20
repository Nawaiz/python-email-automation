import requests
import sys
import webbrowser

def google_search(query, api_key, cse_id):
    print("Googling...")

    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
    }

    try:
        res = requests.get(url, params=params)
        res.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return
    except Exception as err:
        print(f"An error occurred: {err}")
        return

    search_results = res.json()
    link_elems = search_results.get('items', [])

    num_open = min(5, len(link_elems))

    for i in range(num_open):
        webbrowser.open(link_elems[i]['link'])

if len(sys.argv) > 1:
    query = ' '.join(sys.argv[1:])
    api_key = ''  # Replace with your API key
    cse_id = ''  # Replace with your Search Engine ID
    google_search(query, api_key, cse_id)
else:
    print("usage: how.py [search terms]")

