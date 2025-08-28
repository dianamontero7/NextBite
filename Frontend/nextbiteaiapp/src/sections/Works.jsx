import '../Works.css'
import image2 from '../images/womanandfridge.jpg'
import image3 from '../images/dadandgirl.jpg'
import image4 from '../images/womanandmancooking.jpg'

import {Refrigerator, Sparkles, CookingPot} from 'lucide-react';


const Works = () => {

  return(
    <div className='how-it-works'>

    <div className='how-it-works-titles'>
        <h1>How It Works</h1>
        <p>Transform your leftovers into delicious meals in three simple steps</p>
    </div>

    <div className="row row-cols-1 row-cols-md-3 g-4.5">
        
        <div className="col">

          <div className="card h-100">
            <img src={image2} className="card-img-top" alt="Step 1" />
            <div className="card-body">
              <h5 className="card-title"><Refrigerator color="#009966" style={{marginRight: '6.5px'}} /> 1. Tell Us What You Have</h5>
              <p className="card-text">Got leftovers? Tell the generator what you have—like ‘rice, chicken, broccoli.’ Choose meal size, type, servings, dietary preferences, or exclude ingredients, and we’ll craft the perfect recipe.</p>
            </div>
          </div>
        </div>

        <div className="col">
          <div className="card h-100">
            <img src={image3} className="card-img-top" alt="Step 2" />
            <div className="card-body">
              <h5 className="card-title"><Sparkles color="#009966" style={{marginRight: '6.5px'}} /> 2. Get Instant Recipes</h5>
              <p className="card-text">Our AI generator will instantly suggest simple, beginner-friendly recipes based on your ingredients and preferences. Each recipe is easy to follow, requires no fancy tools, and is designed for real-life kitchens.</p>
            </div>
          </div>
        </div>

        <div className="col">
          <div className="card h-100">
            <img src={image4} className="card-img-top" alt="Step 3" />
            <div className="card-body">
              <h5 className="card-title"><CookingPot color="#009966" style={{marginRight: '6.5px'}}/> 3. Start Cooking</h5>
              <p className="card-text">Follow the clear step-by-step instructions and transform your leftovers into something fresh, tasty, and completely stress-free.</p>
            </div>
          </div>
        </div>

    </div>
</div>
  )

}

export default Works;
