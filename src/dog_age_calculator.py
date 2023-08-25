"""Function for calculating dog's age."""

def calculate_dog_age(age, size='small'):
    """
    Calculate a dog's age  represented in human years.

    :param age: int, age in actual years
    :param size: str, small or large size of dog
    :return dog_age: int, age of dog in human years
    """
    if age <= 0:
        raise ValueError(f'{age} is not a valid input, age must be a number higher than 0.')
    elif age == 1:
        dog_age = 15
    elif 1 < age <= 5:
        dog_age = 4 * (age + 4)
    elif age >= 5:
        if size == 'small':
            dog_age = 4 * (age + 4)
        elif size =='large':
            dog_age = 5 * (age + 3)
    print(f'The dog`s age represented in human years is {dog_age}.')
    return dog_age
