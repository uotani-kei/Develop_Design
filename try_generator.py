def try_generator():
    for data in (1, 2, 3, 4, 5):
        yield data
def main():
    for data in (i for i in range(1,6)):
        print(data)
        if data > 2:
            break

if __name__ == "__main__":
    main()