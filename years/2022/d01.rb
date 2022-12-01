# frozen_string_literal: true

testing = false
day = '01'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end


def part1(input)
  data = []
  subtotal = 0
  File.foreach(input).with_index do |line, line_num|
    line = line.chomp
    if line.empty?
      data << subtotal
      subtotal = 0
    else
      subtotal += line.to_i
    end
  end
  data.max
end

puts("Part 1: #{part1(f_input)}")

def part2(input)
  data = []
  subtotal = 0
  File.foreach(input).with_index do |line, line_num|
    line = line.chomp
    if line.empty?
      data << subtotal
      subtotal = 0
    else
      subtotal += line.to_i
    end
  end
  data.sort!.reverse!
  data[0..2].sum
end

puts("Part 2: #{part2(f_input)}")
