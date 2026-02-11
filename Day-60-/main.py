from lru_cache import LRUCache


def main():
    print("Initializing LRU Cache with capacity = 3\n")

    cache = LRUCache(3)

    cache.put(1, "UserA")
    cache.put(2, "UserB")
    cache.put(3, "UserC")

    print("Cache after 3 inserts:")
    print(cache.display())

    print("\nAccess key 2:")
    print("Value:", cache.get(2))
    print("Cache state:")
    print(cache.display())

    print("\nInsert key 4 (should evict least recently used):")
    cache.put(4, "UserD")
    print(cache.display())

    print("\nTrying to access evicted key 1:")
    print("Value:", cache.get(1))  # Should return -1


if __name__ == "__main__":
    main()
