def mirror_xyz(input_file, output_file, plane='yz'):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    atom_count = int(lines[0])
    comment = lines[1].strip()
    atoms = lines[2:]

    mirrored_atoms = []
    for line in atoms:
        parts = line.split()
        if len(parts) < 4:
            continue  # Skip malformed lines
        atom, x, y, z = parts[0], float(parts[1]), float(parts[2]), float(parts[3])

        if plane == 'yz':
            x = -x
        elif plane == 'xz':
            y = -y
        elif plane == 'xy':
            z = -z
        else:
            raise ValueError("Plane must be 'xy', 'yz', or 'xz'")

        mirrored_atoms.append(f"{atom} {x:.6f} {y:.6f} {z:.6f}\n")

    with open(output_file, 'w') as f:
        f.write(f"{atom_count}\n")
        f.write(f"Mirrored across {plane}-plane: {comment}\n")
        f.writelines(mirrored_atoms)

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python mirror_xyz.py input.xyz output.xyz")
    else:
        mirror_xyz(sys.argv[1], sys.argv[2])
