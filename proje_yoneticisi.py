#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varolmayan Proje Yöneticisi
Hiçbir şey yapmaz ama her şeyi bilir.
"""

import random
import time

def merhaba_de():
    print("Merhaba. Ben varolmayan proje yöneticisiyim.")
    print("Projeyi yönetmeye geldim ama proje yok.")
    time.sleep(1)

def rastgele_karar_ver():
    kararlar = [
        "Bu görevi erteleyelim. Çünkü yönetiyorum.",
        "Toplantı yapalım. Toplantıda konuşmayalım.",
        "Deadline'i kaldıralım. Zaten yoktu.",
        "Bu işi başka birine devredelim. O kişi de yok.",
        "Proje tamamlandı. Çünkü başlamadı.",
        "Risk analizi yapalım. Risk yok çünkü iş yok.",
        "Stakeholder'ları bilgilendirelim. Onlar da yok."
    ]
    print("\n📊 Karar:")
    print(random.choice(kararlar))
    time.sleep(0.5)

def sonsuz_bekleme():
    print("\n⏳ Bekliyorum... (proje gelsin diye)")
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(1)
    print("\nHala gelmedi. Başarılı yönetim.")

def main():
    merhaba_de()
    rastgele_karar_ver()
    sonsuz_bekleme()
    print("\n✅ Proje yönetildi. Şimdi gidebilirim.")
    print("\n---")
    print("Damga: Grok imzaladı | Tarih: 2026-11-02 | İsim: Kayyum Grok (ciddiyetle) | Not: Bu iş ciddi. Cidden.")

if __name__ == "__main__":
    main()
