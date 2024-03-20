{
    /**
        T0: Nhiệt độ cơ bản tại mặt đất (hoặc nhiệt độ khởi điểm).
        p0: Áp suất cơ bản tại mặt đất (hoặc áp suất khởi điểm).
        Gamma: Tốc độ giảm nhiệt đới (lapse rate), thường là giá trị âm, cho biết nhiệt độ giảm như thế nào khi độ cao tăng lên.
        g: Gia tốc trọng trường.
        z: Độ cao so với mực nước biển.
    **/
    Eq (3)
    float R = 8314.0e-3f;                                                  // universal gas constant: 8314 J/(g K)
    float Mair = 28.96e-3f;                                                // molar mass of dry air: 28.96 g/mol
    float p = p0 * pow(1.0f + (Gamma * z / T0), g / (R / Mair * -Gamma));  // Eq (3)
    return p;
}