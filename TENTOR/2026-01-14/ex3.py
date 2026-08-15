import sys


def create_pipeline(funcs: list):
    def pipeline(x):
        result = x
        for f in reversed(funcs):
            result = f(result)
        return result

    return pipeline


def check_python_version():
    # ... färdig kod som kollar att du kör rätt version av Python ...
    print(
        f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")


# Hjälpfunktioner
def double(x): return x * 2
def increment(x): return x + 1


def run_tests():
    # De här testerna står uttryckligen som assertions på tentan.
    print("Kör uppgiftens tester...")
    my_pipe = create_pipeline([double, increment])
    # Om vi nu anropar my_pipe(5) ska följande hända:
    # 1. Först appliceras double på 5. Resultat: 10.
    # 2. Sedan appliceras increment på 10. Resultat: 11
    assert my_pipe(5) == 12

    # Om vi byter ordning
    # 1. increment (5) ger 6
    # 2. double (6) ger 12
    my_pipe_reverse = create_pipeline([increment, double])
    assert my_pipe_reverse(5) == 11

    # Om listan av funktioner är tom ska värdet skickas igenom oförändrat.
    empty_pipe = create_pipeline([])
    assert empty_pipe(100) == 100

    # Här lägger du dina egna tester. Du kan till exempel skapa egna
    # assertions, eller lägga till andra tester så som enkla utskrifter
    # av resultatet av en körning.
    print("*"*40)
    print("Kör egna tester...")
    # Single function pipeline
    single_pipe = create_pipeline([double])
    assert single_pipe(5) == 10

    # Single function pipeline with increment
    single_pipe_increment = create_pipeline([increment])
    assert single_pipe_increment(6) == 7

    # Same function repeated multiple times
    repeated_pipe = create_pipeline([double, double])
    assert repeated_pipe(5) == 20

    # Negative input value
    neg_pipe = create_pipeline([double, increment])
    assert neg_pipe(-1) == 0

    # Zero as input
    zero_pipe = create_pipeline([increment, double])
    assert zero_pipe(0) == 1

    # Larger chain of functions, order matters
    def square(x): return x**2
    chain_pipe = create_pipeline([double, increment, square])
    assert chain_pipe(5) == 52

    # Identity-like function that returns input unchanged
    def identity(x): return x
    identity_pipe = create_pipeline([identity])
    assert identity_pipe(42) == 42

    # Pipeline with identity mixed among real functions
    mixed_pipe = create_pipeline([double, increment, identity, square])
    assert mixed_pipe(2) == 10

    # Här kan du lägga tester där du inte vet korrekta svar men
    # ändå kan skriva ut resultatet. Kanske det kraschar, kanske
    # det är uppenbart fel...
    print("*"*40)
    print("Kör utskriftstester...")
    print(empty_pipe(10))  # 10
    print(my_pipe(-1))     # 0

    print("Har kört alla tester")


if __name__ == '__main__':
    check_python_version()
    run_tests()
