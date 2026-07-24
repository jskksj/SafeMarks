"""
core.normalize_scheme
-----------------------
Provides URI normalization functions for the SafeMarks deduplication engine.
"""

from urllib.parse import urlparse, urlunparse

def normalize_scheme(url: str) -> str:
    """
    Canonicalize the transport scheme of a given URL to a secure form.
    
    Converts any variant of 'http' (case-insensitive) to 'https'. Other schemes
    are preserved as-is.
    
    Parameters:
        url (str): The input URL string to normalize.
        
    Returns:
        str: The URL with its transport scheme normalized to https if it was http.
    """
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()
    
    if scheme == "http":
        scheme = "https"
        
    # Reconstruct the URL with the normalized scheme
    return urlunparse((
        scheme,
        parsed.netloc,
        parsed.path,
        parsed.params,
        parsed.query,
        parsed.fragment
    ))