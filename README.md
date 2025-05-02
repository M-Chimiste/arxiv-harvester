# arxiv-harvester

A rate-limit-compliant OAI-PMH harvester for ArXiv papers. This package provides a simple way to harvest metadata from ArXiv papers while respecting their rate limits and handling errors gracefully.

## Features

- Rate-limit compliant (follows ArXiv's policy of ≤ 1 request / 3s)
- Automatic retry with exponential backoff
- Support for resumption tokens and pagination
- Clean Pydantic models for paper metadata
- Optional pandas DataFrame support
- Type hints and comprehensive documentation

## Installation

You can install arxiv-harvester using pip:

```bash
pip install arxiv-harvester
```

To include pandas support for DataFrame conversion:

```bash
pip install arxiv-harvester[pandas]
```

## Quick Start

Here's a simple example to get you started:

```python
from arxiv_harvester import ArxivOAIHarvester

# Create a harvester for AI papers from January 2024
harvester = ArxivOAIHarvester(
    category="cs:AI",
    date_from="2024-01-01",
    date_until="2024-01-31",
    max_results=100,  # Optional: limit the number of results
    verbose=True      # Optional: print progress information
)

# Get the records as a list of dictionaries
records = harvester.harvest()

# Or get them as a pandas DataFrame (requires pandas)
df = harvester.to_dataframe()

# Print some information about the papers
for record in records[:5]:  # First 5 papers
    print(f"Title: {record['title']}")
    print(f"Authors: {', '.join(record['authors'])}")
    print(f"Abstract: {record['abstract'][:200]}...")
    print("-" * 80)
```

## Advanced Usage

### Custom Session

You can provide your own `requests.Session` for custom headers or proxies:

```python
import requests

session = requests.Session()
session.headers.update({
    "User-Agent": "My Research Project (contact@example.com)"
})

harvester = ArxivOAIHarvester(
    category="physics:hep-th",
    date_from="2024-01-01",
    date_until="2024-01-31",
    session=session
)
```

### Retry and Timeout Configuration

Configure retry behavior and timeouts:

```python
harvester = ArxivOAIHarvester(
    category="math:AG",
    date_from="2024-01-01",
    date_until="2024-01-31",
    timeout=600,        # Total operation timeout (seconds)
    base_delay=2.0,    # Base delay between retries
    max_delay=120.0    # Maximum delay between retries
)
```

### Working with Records

Each record contains the following fields:

```python
record = records[0]
print(f"ArXiv ID: {record['id']}")
print(f"Title: {record['title']}")
print(f"Authors: {record['authors']}")
print(f"Abstract: {record['abstract']}")
print(f"Categories: {record['categories']}")
print(f"Created: {record['created']}")
print(f"Updated: {record['updated']}")
print(f"DOI: {record['doi']}")
print(f"URL: {record['url']}")
print(f"PDF URL: {record['pdf_url']}")
print(f"Affiliations: {record['affiliation']}")
```

## Available Categories

ArXiv categories must be specified in colon form. Some common categories include:

- Computer Science: `cs:AI`, `cs:CL`, `cs:CV`, `cs:LG`, etc.
- Physics: `physics:hep-th`, `physics:quant-ph`, etc.
- Mathematics: `math:AG`, `math:AT`, etc.
- Statistics: `stat:ML`, `stat:TH`, etc.

For a complete list of categories, visit [ArXiv's taxonomy](https://arxiv.org/category_taxonomy).

## Rate Limiting

The harvester respects ArXiv's rate limit of 1 request per 3 seconds. It also implements:

- Exponential backoff with jitter for retries
- Proper handling of HTTP 503 responses
- Response to `Retry-After` headers

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache-2.0 License - see the LICENSE file for details.
