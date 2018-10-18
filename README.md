# Symmetric-Cipher-Practice
Python Code for Encrypting and Decrypting simple symmetric ciphers

This is my attempt at creating a program for Encrypting and Decrypting simple plaintext strings.
The Encryption simple randomizes a key and remaps each letter in the the plaintext to another, depending on the key.

The Decryption is an implementation of Hill Climbing. At the start, I calculate letter frequency and compare that with
the most common letters used in English. From there, I continue to "step", randomly swapping letters until I can achieve a higher
score. The scoring system is based on a quadgram analysis.

Unfortunately, I was not able to decipher the given plaintexts for my class, but I imagine an improved scoring algorithm and
the usage of smarter transpositions would improve the success rate.
