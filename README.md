# Instagram Scraper

This script logs into Instagram, retrieves posts based on a specified hashtag, and stores the results in a MongoDB database.

## Requirements

- Python 3
- MongoDB

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AmnaKouki/instagram-scraper
   cd instagram-scraper
   ```

2. Install the required Python packages:
   ```bash
   pip install pymongo instagrapi python-dotenv
   ```

3. Edit the `.env` file and set the following variables:
   ```env
   INSTAGRAM_USERNAME=your_instagram_username
   INSTAGRAM_PASSWORD=your_instagram_password
   MONGO_URI=mongodb://localhost:27017
   MONGO_DB=instagram
   QUERY=cats
   MAX_POSTS=10
   ```

## Usage

1. Run the script:
   ```bash
   python instagram.py
   ```

## Configuration

- `INSTAGRAM_USERNAME`: Your Instagram username.
- `INSTAGRAM_PASSWORD`: Your Instagram password.
- `MONGO_URI`: The URI for your MongoDB instance.
- `MONGO_DB`: The name of the MongoDB database.
- `QUERY`: The hashtag to search for.
- `MAX_POSTS`: The maximum number of posts to retrieve.

## License

This project is licensed under the MIT License.