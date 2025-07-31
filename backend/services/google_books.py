import requests

# Logic to search books from the google book database
def search_books(query: str, max_results: int=5):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        books = []
        
        for item in data.get("items", []):
            volume_info = item["volumeInfo"]
            books.append({
                "title": volume_info.get("title"),
                "authors": volume_info.get("authors"),
                "thumbmail": volume_info.get("imageLinks", {}).get("thumbnail"),
                "description": volume_info.get("description"),
                "publishedDate": volume_info.get("publishedDate"),
                "infoLink": volume_info.get("infoLink"),
            })
        return books

    else:
        return []