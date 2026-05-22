# Script Integrity Verification

<!-- cspell:words keyserver sandboxed -->

This document describes optional methods to verify the integrity of downloaded bootstrap and update scripts before execution.

## Context

When downloading scripts via curl from the internet (e.g., `bash /tmp/bootstrap-copilot.sh`), it is good practice to verify that the script has not been tampered with or corrupted in transit.

## Recommended: SHA-256 Checksum Verification

For each release, a `CHECKSUMS` file is published alongside the release assets.

### Verify before running

```bash
# Download script and checksum
curl -sSfL https://github.com/Hag-Zilla/MyBro/releases/download/v0.1.0/bootstrap-copilot.sh \
  -o /tmp/bootstrap-copilot.sh
curl -sSfL https://github.com/Hag-Zilla/MyBro/releases/download/v0.1.0/CHECKSUMS \
  -o /tmp/CHECKSUMS

# Verify (macOS/BSD: shasum -a 256, Linux: sha256sum)
if command -v sha256sum > /dev/null; then
  (cd /tmp && sha256sum -c CHECKSUMS 2>&1 | grep -q "bootstrap-copilot.sh: OK")
  echo "Checksum valid" || exit 1
else
  # macOS
  (cd /tmp && shasum -a 256 -c CHECKSUMS 2>&1 | grep -q "bootstrap-copilot.sh: OK")
  echo "Checksum valid" || exit 1
fi

# Run only if checksum verified
bash /tmp/bootstrap-copilot.sh
rm /tmp/bootstrap-copilot.sh /tmp/CHECKSUMS
```

## Optional: GPG Signature Verification

For users who require additional assurance, scripts are signed with a project maintainer's GPG key.

### Import the public key

```bash
# Fetch the public key from keyserver
gpg --keyserver keyserver.ubuntu.com --recv-keys <KEY_ID>
```

### Verify a signature

```bash
curl -sSfL https://github.com/Hag-Zilla/MyBro/releases/download/v0.1.0/bootstrap-copilot.sh \
  -o /tmp/bootstrap-copilot.sh
curl -sSfL https://github.com/Hag-Zilla/MyBro/releases/download/v0.1.0/bootstrap-copilot.sh.asc \
  -o /tmp/bootstrap-copilot.sh.asc

gpg --verify /tmp/bootstrap-copilot.sh.asc /tmp/bootstrap-copilot.sh
# Should print: "Good signature from <maintainer>"

bash /tmp/bootstrap-copilot.sh
```

## Future Enhancements

- Automated checksum generation in release workflow
- Optional `--verify-checksum` flag in bootstrap and update scripts
- Lightweight inline checksum validation for pinned releases

## Trust Model

The integrity mechanisms above are designed to defend against:

- Accidental corruption during download
- Man-in-the-middle attacks on the download link
- Tampering with cached scripts

They do **not** substitute for:

- Code review before running downloaded scripts
- Running scripts in isolated or sandboxed environments
- Trusting only scripts downloaded from official releases (avoid pinned URLs to `main`)

## References

- [SHA-256 checksum](https://en.wikipedia.org/wiki/SHA-2)
- [GPG (GNU Privacy Guard)](https://gnupg.org/)
- [Managing releases in a repository](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)
