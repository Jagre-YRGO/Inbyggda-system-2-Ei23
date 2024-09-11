from building import Building

def main():
    print(__name__)

    mitt_hus = Building(2,5,8,"Lärdomsgatan 3")
    print(f'mitt hus har volymen {mitt_hus.calc_volume()}')

if __name__ == '__main__':
    main()