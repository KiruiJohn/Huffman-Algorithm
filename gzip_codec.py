import gzip
import shutil

print("You have the following file options: sample1.txt sample2.txt sample3.txt")
f_name = input("Enter file name: ")

with open(f"./txts/{f_name}", "rb") as f_in:
    with gzip.open(f"./gzipped/{f_name}.gz", "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)