"""
Main script to run the women's tournament scraper
"""
from scraper import TournamentScraper

def main():
    print("Starting Women's Tournament Data Scraper...")
    
    scraper = TournamentScraper()
    
    # Add your target URLs here
    urls = [
        # "https://example.com/womens-tournament",
        # Add more URLs as needed
    ]
    
    for url in urls:
        print(f"Scraping: {url}")
        data = scraper.scrape_tournament_data(url)
        
        if data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"tournament_data_{timestamp}.csv"
            scraper.save_data(data, filename)

if __name__ == "__main__":
    main()
