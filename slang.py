from datetime import datetime

def price_bond(face_value, coupon_rate, maturity_date, discount_rate):
    today = datetime.today()
    maturity = datetime.strptime(maturity_date, "%Y-%m-%d")
    years = int((maturity - today).days / 365)

    coupon_payment = face_value * coupon_rate
    present_value = 0

    for t in range(1, years + 1):
        present_value += coupon_payment / (1 + discount_rate) ** t

    present_value += face_value / (1 + discount_rate) ** years
    return round(present_value, 2)


def main():
    try:
        face_value = float(input("Enter the bond's face value (e.g. 1000): "))
        coupon_percent = float(input("Enter the annual coupon rate (in %, e.g. 5): "))
        maturity_date = input("Enter the maturity date (YYYY-MM-DD, e.g. 2030-12-31): ")
        discount_percent = float(input("Enter the discount rate (in %, e.g. 4.5): "))

        coupon_rate = coupon_percent / 100
        discount_rate = discount_percent / 100

        price = price_bond(face_value, coupon_rate, maturity_date, discount_rate)
        print(f"\n Bond is valued at: ${price}")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    main()
