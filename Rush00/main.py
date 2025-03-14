from checkmate import print_chessboard_with_pieces
from checkmate import movement_patterns
def main():
    board = """\
........
........
........
...K....
........
........
........
.......B\
"""

    result = print_chessboard_with_pieces(board)  # เรียกใช้ฟังก์ชันและรับค่าผลลัพธ์
    result = result.split("\n")# ตัดส่วนเกิน (ถ้ามี "Success" หรือ "Fail")
    
    for row in result:
        print(" ".join(row))  # ใส่ช่องว่างระหว่างตัวอักษร

if __name__ == "__main__":
    main()

if __name__ == "__main__":
    patterns = movement_patterns()
    
    for piece, pattern in patterns.items():
        print(f"Movement Pattern for {piece}:")
        for row in pattern:
            print(row)
        print()

