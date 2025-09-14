using System;

class Converter
{
    static void Main(string[] args)
    {
        string invitation_text =
            @"Here is the list of converter options: 
    1. Convert from °C to °F 
    2. Convert from °F to °C
    3. Convert from miles to kilometres
    4. Convert from kilometres to miles

Choose option from 1 to 4: ";
        Console.Write(invitation_text);
        int input_option = Convert.ToInt32(Console.ReadLine());
        switch (input_option)
        {
            case 1:
                Console.Write("Enter value of temperature in Celsius: ");
                string input_celsius = Console.ReadLine();
                double celsius_converted = Convert.ToDouble(input_celsius);
                float fahrenheit_calc = (float)((celsius_converted * 9 / 5) + 32);
                Console.WriteLine($"Temperature in Fahrenheit: {fahrenheit_calc}°");
                break;
            case 2:
                Console.Write("Enter value of temperature in Fahrenheit: ");
                string input_fahr = Console.ReadLine();
                double fahrenheit_converted = Convert.ToDouble(input_fahr);
                float celsius_calc = (float)((fahrenheit_converted - 32) * 5 / 9);
                Console.WriteLine($"Temperature in Celsius: {celsius_calc}°");
                break;
            case 3:
                Console.Write("Enter value of distance in miles: ");
                string input_miles = Console.ReadLine();
                double miles_converted = Convert.ToDouble(input_miles);
                float km = (float)(miles_converted * 1.60934);
                Console.WriteLine($"Distance in km: {km} kilometres");
                break;
            case 4:
                Console.Write("Enter value of distance in kilometres: ");
                string input_km = Console.ReadLine();
                double km_converted = Convert.ToDouble(input_km);
                float mile = (float)(km_converted * 0.621371);
                Console.WriteLine($"Distance in miles: {mile} miles");
                break;
        }
    }
}


// °F = (°C × 9/5) + 32 option 1.
// °C = (°F - 32) × 5/9 option 2.
// miles * 1.60934
// km * 0.621371