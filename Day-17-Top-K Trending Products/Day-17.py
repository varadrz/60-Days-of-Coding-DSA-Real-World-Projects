# Day 17 - Top-K Trending Products
# Focus: Heap (Priority Queue)
# Language: Python 3

import heapq


def top_k_products(products, k):
    """
    products: list of tuples (product_name, sales_count)
    k: number of top products to return
    """
    min_heap = []

    for product, sales in products:
        heapq.heappush(min_heap, (sales, product))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # Extract results in descending order
    result = sorted(min_heap, reverse=True)
    return result


def main():
    products = [
        ("Laptop", 120),
        ("Mobile", 300),
        ("Headphones", 150),
        ("Smartwatch", 200),
        ("Tablet", 180)
    ]

    k = 3
    top_products = top_k_products(products, k)

    print("\nTop Trending Products:")
    for sales, product in top_products:
        print(f"{product} | Sales: {sales}")


if __name__ == "__main__":
    main()
