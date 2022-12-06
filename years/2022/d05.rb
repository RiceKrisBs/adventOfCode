# frozen_string_literal: true

testing = false
day = '05'

if testing
  f_input = File.join('inputs', "input#{day}-test.txt")
else
  f_input = File.join('inputs', "input#{day}.txt")
end

def part1(input)
  # split input into cargo map and directions
  raw_cargo = []
  raw_directions = []
  File.foreach(input) do |line|
    line.chomp!
    if line.include? 'move'
      raw_directions << line
    elsif line.empty?
      next
    else
      raw_cargo << line
    end
  end

  # create hash that'll store the stacks of boxes
  stacks = Hash.new
  num_stacks = raw_cargo.pop.split.map(&:to_i)[-1]
  (1..num_stacks).each do |val|
    stacks[val] = []
  end

  # parse boxes into their stacks
  raw_cargo.reverse_each do |line|
    (1..num_stacks).each do |stack_num|
      index = 4 * stack_num - 3
      box = line[index]
      unless box.strip.empty?
        stacks[stack_num] << box
      end
    end
  end

  # start moving boxes according to directions
  raw_directions.each do |line|
    _move, num_boxes, _from, start_stack, _to, end_stack = line.split

    num_boxes.to_i.times do |i|
      stacks[end_stack.to_i] << stacks[start_stack.to_i].pop
    end
  end

  letters = []
  (1..num_stacks).each do |i|
    letters << stacks[i][-1]
  end

  letters.join
end

puts("Part 1: #{part1(f_input)}")


def part2(input)
  # split input into cargo map and directions
  raw_cargo = []
  raw_directions = []
  File.foreach(input) do |line|
    line.chomp!
    if line.include? 'move'
      raw_directions << line
    elsif line.empty?
      next
    else
      raw_cargo << line
    end
  end

  # create hash that'll store the stacks of boxes
  stacks = Hash.new
  num_stacks = raw_cargo.pop.split.map(&:to_i)[-1]
  (1..num_stacks).each do |val|
    stacks[val] = []
  end

  # parse boxes into their stacks
  raw_cargo.reverse_each do |line|
    (1..num_stacks).each do |stack_num|
      index = 4 * stack_num - 3
      box = line[index]
      unless box.strip.empty?
        stacks[stack_num] << box
      end
    end
  end

  # start moving boxes according to directions
  raw_directions.each do |line|
    _move, num_boxes, _from, start_stack, _to, end_stack = line.split

    stacks[end_stack.to_i].concat(stacks[start_stack.to_i].pop(num_boxes.to_i))
  end

  letters = []
  (1..num_stacks).each do |i|
    letters << stacks[i][-1]
  end

  letters.join
end

puts("Part 2: #{part2(f_input)}")
