import pytest

from safemarks.core.normalization import normalize_scheme

@pytest.mark.parametrize(
    "input_url, expected_url",
    [
        ("http://example.com", "https://example.com"),
        ("http://example.com/path?query=1", "https://example.com/path?query=1"),
        ("https://example.com", "https://example.com"),
        ("HTTP://example.com", "https://example.com"),
        ("HtTp://Example.Com/", "https://Example.Com/"),
    ],
)
def test_normalize_scheme_converts_http_to_https(input_url, expected_url):
    """Ensure that transport schemes are canonicalized to the secure https form."""
    assert normalize_scheme(input_url) == expected_url

@pytest.mark.parametrize(
    "unsupported_url",
    [
        "ftp://example.com",
        "file:///etc/passwd",
        "mailto:user@example.com",
    ],
)
def test_normalize_scheme_rejects_or_preserves_non_http_schemes(unsupported_url):
    """Ensure non-HTTP/HTTPS schemes are handled gracefully per architecture spec."""
    # Depending on strict design, non-web protocols may either pass through untouched 
    # or raise a ValueError. We assert they do not improperly mutate into http/https.
    result = normalize_scheme(unsupported_url)
    assert not result.startswith("https://") and not result.startswith("http://")
