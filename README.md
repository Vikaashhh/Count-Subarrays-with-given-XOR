# 🔰 Day 50 – GFG 160 Days DSA Challenge
### Problem: Count Subarrays with Given XOR
###  Language: Python
### Date: 1 June 2025

## ✅ Problem Statement:
Given an array of integers and an integer k, determine the count of subarrays whose XOR equals k.

## 💡 Optimized Approach – Prefix XOR + Hash Map:
1. Maintain a running XOR (curr_xor) as we iterate.

2. Use a hash map (xor_map) to track frequencies of XOR results seen so far.

3. For each element:

- Compute required = curr_xor ^ k.

- If required exists in the map, increment the count.

- Update the map with the current XOR value.

This is analogous to the prefix-sum + hashmap method for sum, but adapted for XOR operations.

## ⏱️ Time & Space Complexity:
Time Complexity: O(n)

Space Complexity: O(n)

## 🔖 Hashtags:
#gfg160 #geekstreak2025 #Day50
#xor #prefixxor #dsainpython #hashmap
#framesbyvikash #100daysofcode #pythonchallenge #developerjourney
