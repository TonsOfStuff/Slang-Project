from datetime import datetime

def priceBond(faceValue, couponRate, maturityDate, discountRate):
    today = datetime.today()
    maturity = datetime.strptime(maturityDate, "%Y-%m-%d")
    years = int((maturity - today).days / 365)

    couponPayment = faceValue * couponRate
    presentValue = 0

    for t in range(1, years + 1):
        presentValue += couponPayment / (1 + discountRate) ** t

    presentValue += faceValue / (1 + discountRate) ** years
    return round(presentValue, 2)


def main():
    try:
        faceVal = float(input("Enter the bond's face value (e.g. 1000): "))
        couponPercent = float(input("Enter the annual coupon rate (in %, e.g. 5): "))
        maturityDate = input("Enter the maturity date (YYYY-MM-DD, e.g. 2030-12-31): ")
        discountPercent = float(input("Enter the discount rate (in %, e.g. 4.5): "))

        couponRate = couponPercent / 100
        discountRate = discountPercent / 100

        price = priceBond(faceVal, couponRate, maturityDate, discountRate)
        print(f"\n Bond is valued at: ${price}")

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()
