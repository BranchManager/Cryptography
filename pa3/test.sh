#!/bin/bash

mkdir big_dir
mkdir big_dir/dir1
echo "data in dir1 file1" > big_dir/dir1/file1
echo "data in dir1 file2" > big_dir/dir1/file2
echo "data in dir1 file3" > big_dir/dir1/file3

mkdir big_dir/dir2
mkdir big_dir/dir2/dir2_1
echo "data in dir2 file1" > big_dir/dir2/file1
echo "data in dir2 file2" > big_dir/dir2/file2
echo "data in dir2 file3" > big_dir/dir2/file3

echo "deep check in big_dir/dir2/dir2_1/file1" > big_dir/dir2/dir2_1/file1
mkdir big_dir/dir3
echo "data in dir3 file1" > big_dir/dir3/file1
echo "data in dir3 file2" > big_dir/dir3/file2
echo "data in dir3 file3" > big_dir/dir3/file3

./keygen2 -t rsa -s testing -pub rspub -priv rspriv
./keygen2 -t ec -s testing -pub ecpub -priv ecpriv

./lock -d big_dir -p rspub -r ecpriv -s testing

cat big_dir/dir1/file1
cat big_dir/dir2/file2
cat big_dir/dir3/file3

./unlock -d big_dir -p ecpub -r rspriv -s testing


cat big_dir/dir1/file1
cat big_dir/dir2/file2
cat big_dir/dir3/file3

rm rspub
rm rspriv
rm ecpub
rm ecpriv
