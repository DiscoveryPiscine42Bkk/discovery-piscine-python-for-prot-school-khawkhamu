def print_chessboard_with_pieces(board_string):  # ฟังก์ชันแสดงกระดานหมากรุกและตรวจสอบว่าราชาอยู่ในตำแหน่งอันตรายหรือไม่
    size = 8  # กำหนดขนาดของกระดานหมากรุก (8x8)
    board_rows = board_string.strip().split("\n")  # แปลงสตริงกระดานหมากรุกเป็นลิสต์ของแถว
    
    pieces = {}  # สร้าง dictionary เก็บตำแหน่งของหมาก
    king_position = None  # ตัวแปรเก็บตำแหน่งของราชา
    for row in range(size):  # วนลูปตามแถวของกระดาน
        for col in range(size):  # วนลูปตามคอลัมน์ของกระดาน
            piece = board_rows[row][col]  # อ่านค่าหมากที่ตำแหน่ง (row, col)
            if piece == "K":  # ถ้าเป็นราชา
                king_position = (row, col)  # บันทึกตำแหน่งของราชา
            elif piece in "PBRQ":  # ถ้าเป็นหมากอื่น ๆ (Pawn, Bishop, Rook, Queen)
                pieces[piece] = (row, col)  # บันทึกตำแหน่งของหมาก
    
    directions = {  # กำหนดทิศทางการเดินของหมาก
        "up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1),
        "up_left": (-1, -1), "up_right": (-1, 1), "down_left": (1, -1), "down_right": (1, 1)
    }
    
    def get_attack_positions(piece, position):  # ฟังก์ชันหาตำแหน่งที่หมากสามารถโจมตีได้
        attacks = set()  # ใช้ set เก็บตำแหน่งที่สามารถโจมตีได้
        row, col = position  # กำหนดค่า row และ col จากตำแหน่งที่รับมา
        
        if piece == "P":  # Pawn สามารถโจมตีแนวทแยงหน้าได้
            for direction in ["up_left", "up_right"]:  # Pawn โจมตีได้สองทิศทาง
                dr, dc = directions[direction]  # ค่าการเปลี่ยนแปลง row, col ตามทิศทาง
                r, c = row + dr, col + dc  # คำนวณตำแหน่งใหม่
                if 0 <= r < size and 0 <= c < size:  # ตรวจสอบว่าอยู่ในขอบเขตของกระดาน
                    attacks.add((r, c))  # เพิ่มตำแหน่งที่โจมตีได้ลงใน set
        elif piece == "B":  # Bishop สามารถโจมตีแนวทแยงได้
            for direction in ["up_left", "up_right", "down_left", "down_right"]:
                dr, dc = directions[direction]  # ค่าการเปลี่ยนแปลง row, col
                r, c = row, col  # เริ่มจากตำแหน่งปัจจุบัน
                while 0 <= r + dr < size and 0 <= c + dc < size:  # ตรวจสอบขอบเขต
                    r += dr
                    c += dc
                    attacks.add((r, c))
        elif piece == "R":  # Rook สามารถโจมตีแนวตั้งและแนวนอนได้
            for direction in ["up", "down", "left", "right"]:
                dr, dc = directions[direction]
                r, c = row, col
                while 0 <= r + dr < size and 0 <= c + dc < size:
                    r += dr
                    c += dc
                    attacks.add((r, c))
        elif piece == "Q":  # Queen สามารถโจมตีได้ทั้งแนวตั้ง แนวนอน และแนวทแยง
            for direction in directions:
                dr, dc = directions[direction]
                r, c = row, col
                while 0 <= r + dr < size and 0 <= c + dc < size:
                    r += dr
                    c += dc
                    attacks.add((r, c))
        
        return attacks  # คืนค่าตำแหน่งที่โจมตีได้
    
    attack_positions = set()  # สร้างเซ็ตเก็บตำแหน่งที่ถูกโจมตี
    for piece, pos in pieces.items():  # วนลูปเช็คหมากแต่ละตัว
        attack_positions.update(get_attack_positions(piece, pos))  # รวมตำแหน่งที่โจมตีได้
    
    is_in_check = king_position in attack_positions if king_position else False  # ตรวจสอบว่าราชาอยู่ในตำแหน่งอันตรายหรือไม่
    
    board_display = [["." for _ in range(size)] for _ in range(size)]  # สร้างกระดานเปล่า
    for piece, pos in pieces.items():  # วางหมากบนกระดาน
        board_display[pos[0]][pos[1]] = piece
    if king_position:
        board_display[king_position[0]][king_position[1]] = "K"
    
    for r, c in attack_positions:  # วางเครื่องหมาย x ในตำแหน่งที่ถูกโจมตี
        if board_display[r][c] == ".":
            board_display[r][c] = "x"
    
    board_str = "\n".join("".join(row) for row in board_display)  # แปลงกระดานเป็นสตริง
    board_str += "\n" + ("Success" if is_in_check else "Fail")  # เพิ่มผลลัพธ์ว่าอยู่ในตำแหน่งอันตรายหรือไม่
    
    return board_str  # คืนค่ากระดานที่สร้างเสร็จแล้ว

def movement_patterns():  # ฟังก์ชันแสดงรูปแบบการเดินของหมากแต่ละตัว
    patterns = {
        "P": [
            ". . . . . . . .",
            ". . . . . . . .",
            ". . X . X . . .",
            ". . . P . . . .",
            ". . . . . . . .",
            ". . . . . . . .",
            ". . . . . . . ."
        ],
        "B": [
            "X . . . . . X .",
            ". X . . . X . .",
            ". . X . X . . .",
            ". . . B . . . .",
            ". . X . X . . .",
            ". X . . . X . .",
            "X . . . . . X ."
        ],
        "R": [
            ". . . X . . . .",
            ". . . X . . . .",
            ". . . X . . . .",
            "X X X R X X X .",
            ". . . X . . . .",
            ". . . X . . . .",
            ". . . X . . . ."
        ],
        "Q": [
            "X . . X . . X .",
            ". X . X . X . .",
            ". . X X X . . .",
            "X X X Q X X X .",
            ". . X X X . . .",
            ". X . X . X . .",
            "X . . X . . X ."
        ]
    }
    return patterns  # คืนค่ารูปแบบการเดินของหมาก
