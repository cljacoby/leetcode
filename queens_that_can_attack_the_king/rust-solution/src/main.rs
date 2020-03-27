extern crate termion;
use termion::{color};

// NOTE: Should RGB print colors be stored on the PieceColor enum?
#[derive(Debug, Clone, Copy)]
enum PieceColor {
    Black, 
    White, 
}

#[derive(Debug, Clone, Copy)]
enum PieceClass {
    Queen,
    King,
}

#[derive(Debug, Clone)]
struct Piece {
    color: PieceColor,
    class: PieceClass,
}

#[derive(Debug, Clone)]
struct Board {
    width: u32,
    height: u32,
    grid: Vec<Vec<Option<Piece>>>,
}

impl Piece {
    pub fn new(class: PieceClass, color: PieceColor) -> Self {
        Self { color, class }
    }

}

impl Board {
    // NOTE: hardcoded width and height
    pub fn new() -> Self {
        let width: usize = 8;
        let height: usize = 8;
        let v = vec![vec![None; width]; height];

        Self {
            width: 8,
            height: 8,
            grid: v,
        }
    }

    pub fn set_cell(&mut self, x: usize, y: usize, piece: Piece) {
        // TODO: Handle index out of bounds
        self.grid[x][y] = Some(piece);
    }

    pub fn print(&self) {
        let mut s = String::new();
        for row in self.grid.iter() {
            let mut first = true;
            for cell in row.iter() {
                if !first {
                    s.push_str(",")
                }
                let mut symbol = String::new();
                if cell.is_none() {
                    symbol.push_str("_");
                } else {
                    let piece = cell.as_ref().unwrap();

                    match piece.color {
                        PieceColor::White => {
                            let tty_white = color::Rgb(255, 255, 255).fg_string();
                            symbol.push_str(&tty_white);
                        }
                        PieceColor::Black => {
                            let tty_black = color::Rgb(165, 0, 0).fg_string();
                            symbol.push_str(&tty_black);
                        }
                    }

                    match piece.class {
                        PieceClass::King => {
                            symbol.push_str("K");
                        }
                        PieceClass::Queen => {
                            symbol.push_str("Q");
                        }
                    }

                    symbol.push_str(color::Reset.fg_str());
                }

                s.push_str(&symbol);
                first = false;
            }
            s.push_str("\n");
        }
        println!("{}", s);
    }

    fn get_pieces(&self, color: PieceColor, class: PieceClass) -> Vec<&Piece> {
        let mut pieces = Vec::new();

        for row in self.grid.iter() {
            for cell in row.iter() {
                if cell.is_none() {
                    continue;
                }
                let piece = cell
                    .as_ref()
                    .unwrap();
                match (piece.color, piece.class) {
                    (PieceColor::Black, PieceClass::Queen) => {
                        pieces.push(piece);
                    },
                    _ => {  },
                }
            }
        }

        pieces
    }
}

#[derive(Debug, Clone)]
struct Solution {}

impl Solution {
    pub fn queens_attackthe_king(queens: Vec<Vec<i32>>, king: Vec<i32>) -> Vec<Vec<i32>> {
        Vec::new()
    }
}

fn main() {
    println!("Hello, world!");
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test_piece() {
        println!("\n--------- START: 'test_piece' ----------");

        let king_black = Piece::new(PieceClass::King, PieceColor::Black);
        println!("{:?}", king_black);

        let queen_white = Piece::new(PieceClass::Queen, PieceColor::White);
        println!("{:?}", queen_white);

        println!("--------- FINISH: 'test_piece' ----------");
    }

    #[test]
    fn test_board_print() {
        println!("\n--------- START: 'test_board_print' ----------");

        let mut board = Board::new();
        board.set_cell(1, 1, Piece::new(PieceClass::Queen, PieceColor::Black));
        board.set_cell(2, 7, Piece::new(PieceClass::King, PieceColor::White));
        board.print();
        
        println!("---------- FINISH: 'test_board_print' ----------");
    }

    #[test]
    fn test_get_pieces() {
        println!("\n--------- START: 'test_get_pieces' ----------");

        let mut board = Board::new();
        let black_queen_coords: Vec<(usize, usize)>= vec![
            (1,1),
            (2,2),
            (3,1),
            (4,6)
        ];
        
        for (x,y) in black_queen_coords {
            board.set_cell(x, y, Piece::new(PieceClass::Queen, PieceColor::Black));
        }

        let black_queens = board.get_pieces(PieceColor::Black, PieceClass::Queen);
        println!("{:?}", black_queens);
        
        println!("---------- FINISH: 'test_get_pieces' ----------");
    }

}
