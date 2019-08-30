value = 'テスト'

print('通常の文字列で変数の値を表示します')
print('value = %s' % value)
print()

print(f'フォーマット済み文字列リテラルで変数の値を表示します')
print(f'value = {value}')

value = 5
print(f'3桁ゼロ埋め: {value:03}')
value = 12345
print(f'右よせ: {value:0>8,}')
print(f'左よせ: {value:0<8,}')
print(f'中央: {value:0^8}')