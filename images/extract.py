import sys
import CoreGraphics as CG

def render_page(pdf_path, page_num, out_path):
    url = CG.CGURLCreateWithFileSystemPath(CG.kCFURLPOSIXPathStyle, pdf_path, False)
    provider = CG.CGDataProviderCreateWithURL(url)
    pdf = CG.CGPDFDocumentCreateWithProvider(provider)
    page = CG.CGPDFDocumentGetPage(pdf, page_num)
    
    rect = CG.CGPDFPageGetBoxRect(page, CG.kCGPDFMediaBox)
    width = int(rect.size.width * 2) # 2x scale
    height = int(rect.size.height * 2)
    
    color_space = CG.CGColorSpaceCreateDeviceRGB()
    ctx = CG.CGBitmapContextCreate(None, width, height, 8, width * 4, color_space, CG.kCGImageAlphaPremultipliedLast)
    
    CG.CGContextSetRGBFillColor(ctx, 1.0, 1.0, 1.0, 1.0)
    CG.CGContextFillRect(ctx, CG.CGRectMake(0, 0, width, height))
    
    CG.CGContextScaleCTM(ctx, 2.0, 2.0)
    CG.CGContextDrawPDFPage(ctx, page)
    
    image = CG.CGBitmapContextCreateImage(ctx)
    out_url = CG.CGURLCreateWithFileSystemPath(CG.kCFURLPOSIXPathStyle, out_path, False)
    dest = CG.CGImageDestinationCreateWithURL(out_url, 'public.png', 1, None)
    CG.CGImageDestinationAddImage(dest, image, None)
    CG.CGImageDestinationFinalize(dest)

if __name__ == '__main__':
    for i in range(1, 4):
        render_page('kandai.pdf', i, f'page_{i}.png')
