#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from neo import NEO
import sys

def main():
    try:
        neo = NEO()
        neo.run()
    except KeyboardInterrupt:
        print("\n\n👋 NEO s'arrête...")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erreur fatale: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()