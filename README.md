# YouTube Thumbnail Downloader

A lightweight Python library for searching YouTube videos **without requiring a YouTube Data API key** and downloading their thumbnails in the highest available quality.

The library uses **yt-dlp** to search YouTube and downloads thumbnails directly from YouTube's image servers.

## Features

* Search YouTube using keywords
* No YouTube API key required
* Download thumbnails in the highest available resolution
* Automatic fallback if `maxresdefault.jpg` is unavailable
* Download thumbnails from multiple videos
* Simple Python API
* Cross-platform (Windows, Linux, macOS)

---

## Installation

### Using uv (Recommended)

Install the project dependencies:

```bash
uv sync
```

If you're installing directly from source:

```bash
git clone https://github.com/<username>/youtube-thumbnail-downloader.git

cd youtube-thumbnail-downloader

uv sync
```

Run the application:

```bash
uv run python main.py
```

---

### Using pip

```bash
pip install -r requirements.txt
```

Run:

```bash
python main.py
```

---

## Dependencies

* Python 3.10+
* yt-dlp
* requests

If installing manually:

```bash
uv add yt-dlp requests
```

or

```bash
pip install yt-dlp requests
```

---

## Project Structure

```
youtube-thumbnail-downloader/
│
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
│
└── thumbnails/
    ├── image1.jpg
    ├── image2.jpg
    └── ...
```

---

## Usage

Edit the configuration inside `main.py`.

```python
SEARCH_QUERY = "cats"
MAX_RESULTS = 100
OUTPUT_DIR = "thumbnails"
```

Then run:

```bash
uv run python main.py
```

The script will:

1. Search YouTube.
2. Retrieve video IDs.
3. Download thumbnails.
4. Save them to the output directory.

---

## Output

```
thumbnails/

001_Cute_Cat.jpg
002_Funny_Cat.jpg
003_Cat_Playing.jpg
...
```

---

## Thumbnail Quality

The downloader attempts to fetch thumbnails in the following order:

1. `maxresdefault.jpg`
2. `sddefault.jpg`
3. `hqdefault.jpg`
4. `mqdefault.jpg`

This ensures the highest available quality is downloaded whenever possible.

---

## Example

```python
SEARCH_QUERY = "landscape photography"

MAX_RESULTS = 50

OUTPUT_DIR = "landscape_thumbnails"
```

Result:

```
landscape_thumbnails/
    001_Mountains.jpg
    002_Sunset.jpg
    ...
```

---

## Limitations

* Only public YouTube videos can be searched.
* Some videos do not provide a maximum-resolution thumbnail.
* Very large searches may be slower because YouTube search results are processed sequentially.
* YouTube may temporarily rate-limit excessive requests.

---

## Development

Clone the repository:

```bash
git clone https://github.com/<username>/youtube-thumbnail-downloader.git
```

Install dependencies:

```bash
uv sync
```

Run the project:

```bash
uv run python main.py
```

Update dependencies:

```bash
uv add <package>
```

Remove a dependency:

```bash
uv remove <package>
```

Run with a temporary package:

```bash
uv run --with requests python script.py
```

---

## Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

This project downloads publicly available thumbnail images from YouTube for educational and research purposes. Users are responsible for complying with YouTube's Terms of Service and respecting applicable copyright laws when using downloaded content.
