# frozen_string_literal: true

require_relative 'base'

class Day < Base
  def part_1
    data = File.read(input).split("\n").map(&:split)
    hands = {
      'five-of-a-kind' => [],
      'four-of-a-kind' => [],
      'full-house' => [],
      'three-of-a-kind' => [],
      'two-pair' => [],
      'one-pair' => [],
      'high-card' => []
    }
    data.map do |line|
      cards = line[0]
      
      hand_type = calculate_part_one_hand(cards)
      hands[hand_type] << line
    end

    hands.keys.each do |key|
      hands[key] = hands[key].sort do |a, b|
        transform_hand(a.first, RANKING) <=> transform_hand(b.first, RANKING)
      end
    end

    all_hands = []
    hands.values.each do |hand|
      all_hands.push(*hand)
    end

    all_hands.reverse!

    total = 0
    all_hands.each_with_index do |hand, index|
      total += (index + 1) * hand.last.to_i
    end

    throw 'wrong part 1' unless total == 251545216
    total
  end

  def part_2
    data = File.read(input).split("\n").map(&:split)
    hands = {
      'five-of-a-kind' => [],
      'four-of-a-kind' => [],
      'full-house' => [],
      'three-of-a-kind' => [],
      'two-pair' => [],
      'one-pair' => [],
      'high-card' => []
    }
    data.map do |line|
      cards = line[0]
      
      hand_type = calculate_part_two_hand(cards)
      hands[hand_type] << line
    end

    hands.keys.each do |key|
      hands[key] = hands[key].sort do |a, b|
        transform_hand(a.first, WILD_RANKING) <=> transform_hand(b.first, WILD_RANKING)
      end
    end

    all_hands = []
    hands.values.each do |hand|
      all_hands.push(*hand)
    end

    all_hands.reverse!

    total = 0
    all_hands.each_with_index do |hand, index|
      total += (index + 1) * hand.last.to_i
    end

    throw 'wrong part 2' unless total == 250384185
    total
  end

  private

  TESTING = false
  DAY = '07'

  RANKING = %w[A K Q J T 9 8 7 6 5 4 3 2]
  WILD_RANKING = %w[A K Q T 9 8 7 6 5 4 3 2 J]
  
  def input
    TESTING ? File.join('inputs', "input#{DAY}-test.txt") : File.join('inputs', "input#{DAY}.txt")
  end

  def card_count(hand)
    h = {}
    hand.chars.each do |card|
      h[card] = h[card] || 0
      h[card] += 1
    end
    h.sort_by { |k,v| -v }
  end

  def transform_hand(hand, transform)
    hand.each_char.map  { |c| transform.index(c)}
  end

  def calculate_part_one_hand(hand)
    return 'high-card' if hand == ''
    count = card_count(hand)
    if count[0][1] == 5
      'five-of-a-kind'
    elsif count[0][1] == 4
      'four-of-a-kind'
    elsif count.length > 1 && count[0][1] == 3 && count[1][1] == 2
      'full-house'
    elsif count[0][1] == 3
      'three-of-a-kind'
    elsif count.length > 1 && count[0][1] == 2 && count[1][1] == 2
      'two-pair'
    elsif count[0][1] == 2
      'one-pair'
    else
      'high-card'
    end
  end

  def calculate_part_two_hand(hand)
    joker_count = hand.count('J')
    hand_without_jokers = hand.gsub('J', '')
    hand_type_without_jokers = calculate_part_one_hand(hand_without_jokers)
    case joker_count
    when 0 # 5 cards to consider
      return hand_type_without_jokers
    when 1 # 4 cards to consider
      return 'one-pair' if hand_type_without_jokers == 'high-card'
      return 'three-of-a-kind' if hand_type_without_jokers == 'one-pair'
      return 'full-house' if hand_type_without_jokers == 'two-pair'
      return 'four-of-a-kind' if hand_type_without_jokers == 'three-of-a-kind'
      return 'five-of-a-kind' if hand_type_without_jokers == 'four-of-a-kind'
    when 2 # 3 cards to consider
      return 'three-of-a-kind' if hand_type_without_jokers == 'high-card'
      return 'four-of-a-kind' if hand_type_without_jokers == 'one-pair'
      return 'five-of-a-kind' if hand_type_without_jokers == 'three-of-a-kind'
    when 3 # 2 cards to consider
      return 'four-of-a-kind' if hand_type_without_jokers == 'high-card'
      return 'five-of-a-kind' if hand_type_without_jokers == 'one-pair'
    when 4 # 1 card to consider
      return 'five-of-a-kind' if hand_type_without_jokers == 'high-card'
    when 5 # 0 cards to consider
      return 'five-of-a-kind' if hand_type_without_jokers == 'high-card'
    end
  end
end

Day.new.run
# Day.new.benchmark
