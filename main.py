import sys
from Serie_reducida import evaluar

def main() -> int:
    evaluar()
    return 0  # Siempre retorna un int para que sys.exit tenga sentido

if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n*** FIN ***")
        sys.exit(0)
