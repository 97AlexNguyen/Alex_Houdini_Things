{
    /**
        T0: Nhiệt độ cơ bản tại mặt đất (hoặc nhiệt độ khởi điểm).
        p0: Áp suất cơ bản tại mặt đất (hoặc áp suất khởi điểm).
        Gamma: Tốc độ giảm nhiệt đới (lapse rate), thường là giá trị âm, cho biết nhiệt độ giảm như thế nào khi độ cao tăng lên.
        g: trọng lực 
        z: Độ cao 
    **/
    Eq (3)
    float R = 8314.0e-3f;                                                 
    float Mair = 28.96e-3f;                                                
    float p = p0 * pow(1.0f + (Gamma * z / T0), g / (R / Mair * -Gamma));  
    return p;
}
