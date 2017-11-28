class ShrinkersController < ApplicationController
  # Just for testing it with postman. Remove it once done.
  protect_from_forgery except: :shrink


  def shrink
    original_url = params[:url][:original]
    puts original_url
  end

end
