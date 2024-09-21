# Curriculum Project: Caching Algorithms

## [C#22] Spe - Web Stack Programming 2024

---

## Background Context

In this project, we will learn about various caching algorithms and their implementations. Caching is a critical component of web development and system design, enhancing performance by temporarily storing frequently accessed data.

---

## Learning Objectives

At the end of this project, we should be able to explain the following concepts clearly:

- **What a caching system is**
- **Caching Policies:**
  - FIFO (First In, First Out)
  - LIFO (Last In, First Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)
- **The purpose of a caching system**
- **The limitations of caching systems**

---

## Resources

Read or watch the following materials to deepen our understanding:


- <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29" target="_blank">Cache Replacement Policies - FIFO</a><br>
- <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29" target="_blank">Cache Replacement Policies - LIFO</a><br>
- <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29" target="_blank">Cache Replacement Policies - LRU</a><br>
- <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29" target="_blank">Cache Replacement Policies - MRU</a><br>
- <a href="https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29" target="_blank">Cache Replacement Policies - LFU</a>


---

## Requirements

- **Python Scripts**:
  - All files must be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3** (version 3.9).
  - Each file should end with a new line.
  - The first line of all files should be exactly: `#!/usr/bin/env python3`
  - A `README.md` file at the root of the project folder is mandatory.
  - Our code should adhere to the **pycodestyle** style (version 2.5).
  - All files must be executable.
  - The length of our files will be verified using `wc`.
  - All modules, classes, and functions must have documentation.
    - Use the following commands to verify:
      - `python3 -c 'print(__import__("my_module").__doc__)'`
      - `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
      - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`

---

## BaseCaching Parent Class

All our classes must inherit from `BaseCaching`, defined as follows:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching:
    """ BaseCaching defines:
      - constants of our caching system
      - where our data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize the cache system
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the current cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in our cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in our cache class")
```

## Conclusion

This project aims to equip us with a thorough understanding of caching algorithms and their practical implementations. We are encouraged to explore and implement the various caching strategies as part of our learning journey.

## Acknowledgments

Thanks to Guillaume, CTO at Holberton School, for guiding the project.
