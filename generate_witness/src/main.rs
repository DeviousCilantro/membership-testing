use rug::Integer;
use std::io::{self, BufRead, Write};
use std::fs::File;
use std::path::Path;
use sha2::{Digest, Sha256};
use std::collections::HashMap;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn hash_to_prime(data: &str) -> Integer {
    let mut hasher = Sha256::new();
    hasher.update(data);
    Integer::from_str_radix(&format!("{:x}", hasher.finalize()), 16).unwrap().next_prime()
}

fn generate_witness(g: &Integer, n: &Integer) {
    let mut prime_elements: Vec<Integer> = Vec::new();
    let mut witnesses: HashMap<String, Integer> = HashMap::new();
    if let Ok(lines) = read_lines("emails.txt") {
        for email in lines.flatten() {
            let prime = hash_to_prime(&email);
            prime_elements.push(prime);
        }
    }
    if let Ok(lines) = read_lines("emails.txt") {
        for email in lines.flatten() {
            let mut product = Integer::from(1);
            for (index, element) in prime_elements.iter().enumerate() {
                let prime = hash_to_prime(&email);
                if index != prime_elements.iter().position(|x| x == &prime).unwrap() {
                    product *= element;
                }
            }
            witnesses.insert(email.clone(), g.clone().secure_pow_mod(&product, n));
        }
        println!("Generated membership witnesses.");
        for (key, value) in &witnesses {
            println!("{key}: {value}");
        }
    }
}

fn main() {
    let mut input = String::new();
    print!("Enter the rigid integer value: ");
    io::stdout().flush().unwrap();
    std::io::stdin()
        .read_line(&mut input)
        .unwrap();
    let n = Integer::from_str_radix(input.trim(), 10).unwrap();
    print!("Enter the base value: ");
    io::stdout().flush().unwrap();
    std::io::stdin()
        .read_line(&mut input)
        .unwrap();
    let g = Integer::from_str_radix(input.trim(), 10).unwrap();
    generate_witness(&g, &n);
}
