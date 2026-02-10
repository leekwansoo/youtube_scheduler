def add(a, b):
    """덧셈 연산"""
    return a + b

def subtract(a, b):
    """뺄셈 연산"""
    return a - b

def multiply(a, b):
    """곱셈 연산"""
    return a * b

def modulo(a, b):
    """나머지 연산"""
    if b == 0:
        return "오류: 0으로 나눌 수 없습니다!"
    return a % b

def get_number_input(prompt):
    """사용자로부터 숫자 입력 받기"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("올바른 숫자를 입력해주세요!")

def display_menu():
    """계산기 메뉴 출력"""
    print("\n" + "="*40)
    print("        간단한 사칙연산 계산기")
    print("="*40)
    print("1. 덧셈 (+)")
    print("2. 뺄셈 (-)")
    print("3. 곱셈 (*)")
    print("4. 나머지 (%, 모듈로)")
    print("5. 종료")
    print("="*40)

def main():
    """메인 계산기 함수"""
    print("사칙연산 계산기에 오신 것을 환영합니다!")
    
    while True:
        display_menu()
        
        try:
            choice = input("원하는 연산을 선택하세요 (1-5): ").strip()
            
            if choice == '5':
                print("계산기를 종료합니다. 안녕히가세요! 👋")
                break
            
            if choice not in ['1', '2', '3', '4']:
                print("잘못된 선택입니다. 1-5 사이의 숫자를 선택해주세요.")
                continue
            
            # 숫자 입력 받기
            num1 = get_number_input("첫 번째 숫자를 입력하세요: ")
            num2 = get_number_input("두 번째 숫자를 입력하세요: ")
            
            # 연산 수행
            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2}"
            elif choice == '4':
                result = modulo(num1, num2)
                operation = f"{num1} % {num2}"
            
            # 결과 출력
            print(f"\n📊 계산 결과: {operation} = {result}")
            
            # 계속할지 묻기
            continue_calc = input("\n다른 계산을 하시겠습니까? (y/n): ").strip().lower()
            if continue_calc not in ['y', 'yes', '예', 'ㅇ']:
                print("계산기를 종료합니다. 감사합니다! 👋")
                break
                
        except KeyboardInterrupt:
            print("\n\n계산기를 종료합니다. 안녕히가세요! 👋")
            break
        except Exception as e:
            print(f"오류가 발생했습니다: {e}")
            print("다시 시도해주세요.")

if __name__ == "__main__":
    main()