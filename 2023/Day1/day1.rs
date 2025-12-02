use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn lines_from_file(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line"))
        .collect()
}

fn part_one(input : Vec<String>) -> u32 {
    let mut sum = 0;
    for line in input{
        for char in line.chars(){
            if char.is_digit(10){
                sum += 10 * char.to_digit(10);
                break;
            }
        }
        for char in line.chars().rev(){
            if char.is_digit(10){
                sum += char.to_digit(10);
                break;
            }
        }
    }
    return sum
}



fn main() {
    let input = lines_from_file("input.txt");

    println!("{}", part_one(input));
}
