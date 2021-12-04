#!/usr/bin/env bb

(ns day3
  (:require [clojure.string :as str]))

(def example-input
  (str/split "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010" #"\s"))
(def my-input (str/split-lines (slurp "input.txt")))

(defn bits->long [bits]
  (read-string (apply str "2r" bits)))

(defn part1 [input]
  (->> input
       (apply map vector)
       (map (partial group-by identity))
       (map (partial sort-by (comp count second)))
       (map ffirst)
       ((juxt identity (partial map {\0 \1 \1 \0})))
       (map bits->long)
       (apply *)))


(prn (part1 example-input) 198)
(prn (part1 my-input) 2954600)


;; part 2
(defn indicator [input choosefn]
  (->> [input 0]
       (iterate
        (fn [[remaining idx]]
          [(->> remaining
                (group-by #(nth % idx))
                (sort-by key)
                (map second)
                (sort-by count)
                (choosefn))
           (inc idx)]))
       (drop-while #(-> % first count (> 1)))
       ffirst
       bits->long))

(defn part2 [input]
  (->> [first last]
       (map (partial indicator input))
       (apply *)))

(prn (part2 example-input) 230)
(prn (part2 my-input) 1662846)
