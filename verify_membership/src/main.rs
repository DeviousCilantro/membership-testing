use rug::Integer;
use std::io::{self, Write};
use sha2::{Digest, Sha256};

fn hash_to_prime(data: &str) -> Integer {
    let mut hasher = Sha256::new();
    hasher.update(data);
    Integer::from_str_radix(&format!("{:x}", hasher.finalize()), 16).unwrap().next_prime()
}

fn verify_membership(n: Integer, acc: Integer, element: Integer, w: Integer) {
    assert_eq!(w.secure_pow_mod(&element, &n), acc, "Membership not verified.");
    println!("Membership verified.");
}

fn main() {
    let mut input = String::new();
    print!("Enter the rigid integer value: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let n = Integer::from_str_radix(input.trim(), 10).unwrap();
    let mut input = String::new();
    print!("Enter the accumulator value: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let acc = Integer::from_str_radix(input.trim(), 10).unwrap();
    let mut input = String::new();
    print!("Enter the email id: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let ele = hash_to_prime(input.trim());
    let mut input = String::new();
    print!("Enter the membership witness value: ");
    io::stdout().flush().unwrap();
    io::stdin()
        .read_line(&mut input)
        .unwrap();
    let w = Integer::from_str_radix(input.trim(), 10).unwrap();
    verify_membership(n, acc, ele, w);
}
