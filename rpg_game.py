import random
import streamlit as st

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack_enemy(self, enemy):
        damage = random.randint(0, self.attack)
        st.write(f"{self.name} menyerang {enemy.name} dan menyebabkan {damage} damage!")
        enemy.take_damage(damage)


def main():
    player = Character("Player", 100, 20)
    monster = Character("Monster", 80, 15)

    st.title("Game RPG Classic")
    st.write("Pemain: ", player.name)
    st.write("Monster: ", monster.name)

    while player.is_alive() and monster.is_alive():
        st.write("\nPemain HP:", player.hp)
        st.write("Monster HP:", monster.hp)
        st.write("\nPilihan Pemain:")
        st.write("1. Serang")
        st.write("2. Istirahat")

        choice = st.selectbox("Apa yang akan Anda lakukan?", ('Serang', 'Istirahat'))

        if choice == 'Serang':
            player.attack_enemy(monster)
            if monster.is_alive():
                monster.attack_enemy(player)
        elif choice == 'Istirahat':
            player.heal(10)
            st.write("Anda beristirahat dan memulihkan 10 HP.")
            monster.attack_enemy(player)

    if player.is_alive():
        st.success("Selamat! Anda menang melawan monster!")
    else:
        st.error("Anda kalah. Monster telah mengalahkan Anda.")

if __name__ == "__main__":
    main()
