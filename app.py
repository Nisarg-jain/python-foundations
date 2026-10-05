"""Filesystem inspection and path manipulation using pathlib."""

from pathlib import Path


def inspect_workspace(target_pattern: str = "*.py") -> None:
    """Scans current workspace directory and lists matching files."""
    current_directory = Path()

    print(f"--- Scanning directory: '{current_directory.resolve().name}' for '{target_pattern}' ---")

    matching_files = list(current_directory.glob(target_pattern))

    if not matching_files:
        print("No files matched the specified pattern.")
        return

    for file_path in matching_files:
        print(f"Found: {file_path.name} (Absolute: {file_path.resolve()})")


def demonstrate_directory_lifecycle(dir_name: str = "temp_store") -> None:
    """Demonstrates defensive directory creation and cleanup."""
    target_dir = Path(dir_name)

    # Check existence before attempting creation
    if not target_dir.exists():
        target_dir.mkdir()
        print(f"\nDirectory created: {target_dir.name}")
    else:
        print(f"\nDirectory already exists: {target_dir.name}")

    # Clean up created test directory
    if target_dir.exists():
        target_dir.rmdir()
        print(f"Directory cleaned up: {target_dir.name}")


if __name__ == "__main__":
    inspect_workspace("*.py")
    demonstrate_directory_lifecycle()