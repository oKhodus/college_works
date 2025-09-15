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
    5. Convert from inches to centimetres
    6. Convert from centimetres to inches
    7. Convert from pounds to kilogrammes
    8. Convert from kilogrammes to pounds

Choose option from 1 to 8: ";
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
                Console.WriteLine($"Distance in km: {km} km");
                break;
            case 4:
                Console.Write("Enter value of distance in kilometres: ");
                string input_km = Console.ReadLine();
                double km_converted = Convert.ToDouble(input_km);
                float mile = (float)(km_converted * 0.621371);
                Console.WriteLine($"Distance in miles: {mile} miles");
                break;
            case 5:
                Console.Write("Enter value of distance in inches: ");
                string input_inch = Console.ReadLine();
                double inch_converted = Convert.ToDouble(input_inch);
                float cm = (float)(inch_converted * 2.54);
                Console.WriteLine($"Distance in centimetres: {cm} cm");
                break;
            case 6:
                Console.Write("Enter value of distance in centimetres: ");
                string input_cm = Console.ReadLine();
                double cm_converted = Convert.ToDouble(input_cm);
                float inch = (float)(cm_converted / 2.54);
                Console.WriteLine($"Distance in inches: {inch} in");
                break;
            case 7:
                Console.Write("Enter value of weight in pounds: ");
                string input_pound = Console.ReadLine();
                double pound_conv = Convert.ToDouble(input_pound);
                float kg = (float)(pound_conv * 0.45359237);
                Console.WriteLine($"Weight in kilogrammes: {kg} kg");
                break;
            case 8:
                Console.Write("Enter value of weight in kilogrammes: ");
                string input_kg = Console.ReadLine();
                double kg_conv = Convert.ToDouble(input_kg);
                float pound = (float)(kg_conv * 2.20462);
                Console.WriteLine($"Weight in pounds: {pound} lb");
                break;
        }
    }
}


// °F = (°C × 9/5) + 32 option 1.
// °C = (°F - 32) × 5/9 option 2.
// miles * 1.60934
// km * 0.621371
// cm / 2.54
// inch * 2.54
// Kilograms = Pounds × 0.45359237
// Pounds = Kilograms × 2.20462