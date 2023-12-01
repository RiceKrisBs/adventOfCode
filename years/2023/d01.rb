# frozen_string_literal: true


class Day
  def part_1
    data = File.read(input).split("\n")
    data.map do |line|
      nums = line.scan(/\d/)
      "#{nums.first}#{nums.last}".to_i
    end.sum
  end

  def part_2
    data = File.read(input).split("\n")
    data.map do |line|
      "#{first_num(line)}#{last_num(line)}".to_i
    end.sum
  end

  private

  TESTING = false
  DAY = '01'
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def first_num(line)
    # find the first number or word by looking for the lowest index
    # of a number or word
    num_idx = line.index(/\d/) || (line.length + 1) # if not found, make unusablely large
  
    words = %w(one two three four five six seven eight nine)
    word_idxs = {}
    words.each do |word|
      word_idxs[word] = line.index(word)
    end
    min_word_idx = word_idxs.values.compact.min || (line.length + 1)
  
    if num_idx < min_word_idx
      line[num_idx].to_i
    else
      word_to_num(word_idxs.key(min_word_idx))
    end
  end

  def last_num(line)
    # find the last number or word by looking for the highest index
    # of a number or word
    num_idx = line.rindex(/\d/) || -1 # if not found, make unusablely small
  
    words = %w(one two three four five six seven eight nine)
    word_idxs = {}
    words.each do |word|
      word_idxs[word] = line.rindex(word)
    end
    max_word_idx = word_idxs.values.compact.max || -1
  
    if num_idx > max_word_idx
      line[num_idx].to_i
    else
      word_to_num(word_idxs.key(max_word_idx))
    end
  end

  def word_to_num(word)
    nums = %w(zero one two three four five six seven eight nine)
    nums.index(word).to_i
  end
end

puts("Part 1: #{Day.new.part_1}")
puts("Part 2: #{Day.new.part_2}")
