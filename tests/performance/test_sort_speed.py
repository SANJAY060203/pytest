def test_sorting_speed(benchmark):
    benchmark(sorted, list(range(1000, 0, -1)))
