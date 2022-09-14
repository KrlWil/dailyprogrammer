// See https://aka.ms/new-console-template for more information

Console.WriteLine(yahtzee_upper(new List<int>() {2, 3, 5, 5, 6}));
Console.WriteLine(yahtzee_upper(new List<int>() {1, 1, 1, 1, 3}));
Console.WriteLine(yahtzee_upper(new List<int>() {1, 1, 1, 3, 3}));
Console.WriteLine(yahtzee_upper(new List<int>() {1, 2, 3, 4, 5}));
Console.WriteLine(yahtzee_upper(new List<int>() {6, 6, 6, 6, 6}));

static int yahtzee_upper (List<int> dice)
{
    // group dice, calculate value * Count and return the max value
    return dice.GroupBy(i => i).Select(i => i.Key * i.ToList().Count).Max();;
}