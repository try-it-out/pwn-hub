import os

if __name__ == "__main__":
  print(f"It works - {os.environ.get('BUCKET_NAME')}")