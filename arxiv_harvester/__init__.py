"""
arxiv-harvester - A rate-limit-compliant OAI-PMH harvester for ArXiv papers.

This package provides tools to harvest metadata from ArXiv papers using their OAI-PMH API,
while respecting rate limits and handling errors gracefully.
"""

from arxiv_harvester.harvester import ArxivOAIHarvester, Record

__version__ = "0.1.1"
__all__ = ["ArxivOAIHarvester", "Record"]
